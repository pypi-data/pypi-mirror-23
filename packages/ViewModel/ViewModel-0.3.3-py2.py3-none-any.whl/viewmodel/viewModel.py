from collections import OrderedDict as ODict
from enum import Enum

from bson.objectid import ObjectId
from objdict import (ObjDict)


from viewmodel.viewFields import BaseField, Case, FieldItem


Section = Enum('ViewSection', 'all header main footer')
# 'edit' in Case.__members__
# try:
#     import saltMongDB as viewModelDB
# except ImportError:
from .viewFields import viewModelDB

class ViewModelError(Exception):
    def __init__(self, message, **extras):
        Exception.__init__(self, message)
        self.extras = extras

def get_dict_attr(obj, attr):
    for obj in [obj]+obj.__class__.mro():
        if attr in obj.__dict__:
            return obj.__dict__[attr]
    raise AttributeError

class BaseFieldDict(ODict):
    def __init__(self, *args, **kwargs ):
        super().__init__(*args, **kwargs)

    #code

class PageDict(ODict):
    """ PageDict is a dict of all fields in view, including all rows
    in the view!
    """
    def __init__(self, view, basef, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.view = view
        self.main = ODict() #this should be all rows
        self.head = ODict()
        self.foot = ODict()
        cdict = self.main
        self.Section = Section
        self.Case = Case
    def __2call__(self, *args, **kwargs):
        self.view.loop(*args, **kwargs)

    def __call__(self, section=Section.main, case=Case.viewAll):
        view = self.view

        if section in (Section.all, Section.header):
            for name,field in self.head.items():
                if field.cases is None or case in field.cases:
                    yield field

        if section in (Section.all, Section.main):
            doAll = True #- do_all_rows  :was-> = section is not Section.current
            count = len(view.dbRows_)
            save=view.idx_
            for i in range(count):
                for name,field in self.main.items():
                    if field.cases is None or case in field.cases:
                        yield field

        if section in (Section.all, Section.footer):
            for name,field in self.foot.items():
                if field.cases is None or case in field.cases:
                    yield field

class FieldDict(ODict):
    def __init__(self, view, basef, row, *args, **kwargs ):
        super().__init__(*args,**kwargs)
        self.view=view
        self.Case=Case
        for nm,f in basef.items():
            self[nm]=FieldItem(view,f,row)

    def __2call__(self,*args,**kwargs):
        self.view.loop(*args,**kwargs)

    def __call__(self,case=Case.viewAll ):
        view=self.view

        for name,field in self.items():
            if field.cases is None or case in field.cases or case == Case.allFields:
                yield field

    def loopRows(self):
        """ an iterator to set each row in turn as current
        does not actually belong here- but in View itself!
        """
        for i in range(len(self.view.dbRows_)):
            yield ViewRow(self.view,i)

class ViewRow:
    """ the idea is to have a view
    consist, at least logically, of a number of view rows.
    so view[n]  is the nth row:
    .    this would allow an improved interation through a view
    .    plus allow storing references to a specific row within a view.
    each view could still have a 'default' row which can be set by
    "idx _" as happens currently

    so for example- an actual view could really be a view row
    which returns a new view row object when indexed. the new viewrow object
    would have the same data for all except _idx?  copy object, reset idx?
    would that work? would share rows and fields. what else would not be shared
    so viewObj[1] is copy of view with _idx set to 1?

    this would be neater if what was instanced was::

        view self._idx,self.underlying_view

    """
    def __init__(self, view, row):
        self._view = view
        self._row = row
        self._fields = None
        #self.__json__encode = None

    def __getattr__(self, attr):
        # if bug makes recurse then check attrs are ViewFields!
        if attr in self.fields_:
            return self._view._baseFields[attr].__get__(self._view, None, self._row)
        raise AttributeError('no {} in ViewRow'.format(attr))

    def __setattr__(self, attr, value):
        if attr in ('_view', '_row', '_fields'):
            super().__setattr__(attr, value)
        elif attr in ('idx_',):
            raise AttributeError('Cant set '+ attr)
        elif attr in self.fields_:
            self._view._baseFields[attr].__set__(self._view, value, self._row)
        else:
            raise TypeError('Whoa - ViewRow Attr error')

    @property
    def labelsList_(self):  #this should be deprecated...was a mistake to add here
        return self._view.labelsList_

    @property
    def rowLabel_(self):
        pass

    @property
    def idx_(self):
        return self._row

    @property
    def view_(self):
        return self._view

    @property
    def fields_(self):
        if self._fields == None:
            self._fields = FieldDict(self._view,self._view._baseFields,self._row)
        return self._fields

    def __getitem__(self,key):
        return self.fields_[key]

    def update_(self):
        self._view.update_()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.update_()

    def __iter__(self):
        return self.fields_()

    def loop_(self,case=Case.viewAll, section=Section.all ):
        #section is an idea - but not yet implemented
        return self.fields_(case=case)
        # group = [self.fields_,self.head,self.main.self.foot][section]
        # for field in group:
        #     if field.cases is None or case in field.cases:
        #         yield field

    def __json__(self, internal=False):
        res = dict(ViewRow=self.__class__.__name__)
        if not internal:
            res=str(res)
        return res


class DBSource:
    """
        consists of an ObjDict keyed by what was 'joins', but with an entry for all tables
        with each entry being an object with 'row_source', and 'row_key' attributes.
        row_source - is the previous dbRowSrc_  ...the table object for db operations
            row_source set to none should be used to indicate a memory only source
        row_id - None except when view data is embedded in a list within a single
                document, in which case this is the key for the umbrella document

        loader  -  the method to be used to lazy load the data
        join_links  - list of ViewFlds to be updated with _id
    """


    #__keys__ = "full_name row_source row_id"
    loader = None
    def __init__(self, full_name, row_source, row_id):
        self.full_name = full_name
        self._row_source = row_source
        self.row_id = row_id
        self.join_links = []

    def __repr__(self):
        return ('DBSource: {full_name} from {_row_source} id:{row_id} j:{join_links}'
                .format(**vars(self)))
    
    @property
    def row_source(self):
        return None

    def map_src(self, src):
        """ maps a 'src' string to return dictionary names
          currently simply assumes first link is source and correct
          so discards first link"""
        return src.split('.')[1:]

    def save_change(self, view, idx_, change, tbl):
        return # default is to ignore changes
class DBNoSource(DBSource):
    pass

from viewmodel.viewMongoSources import DBMongoSource

class BaseView:
    """ a view is an object model containing view specific model in addition
    to potentially one or more database row models.
    Joins views are launched with the base join table
    or directly.  if a view is instanced directly- then 'join' fields are not
    available, and access will be an error
    As properites of any name can be added and should not colide with

    A view is usually specific to one or mode data base rows, but allows for operations (such as 'next')
    to change the database row appearing in the view.
    Views can be input as well as output.
    View fields values can be retrieved and set as properties within the view, but can also be accessed from

    _baseFields {}   class property, is an ordered dict of all 'field' properites sorted by order
    fields_  {}      is an instance object controlling access to odict  (property,instance) 
    .                pairs for accessing:
    .                both value and properties of a field
    joins_ {}      if rows are collections built from joins,
    .                objdict of loaders that contain the actual rows.
    .                field searches occur in order of the list
    _sources {}  a new ObjDict of DBSource objects which replaces 'joins' and dbRowSrc 
    dbRows_  is a list of rows, with each row an ObjDict keyed by source, containing the values
    .              for each source.  Normally values for each source are also an ObjDict, but
    .              future types could change this
    """
    _baseFields = None

    def __init__(self, *args, **kwargs):
        self._sources = ObjDict()
        models = kwargs.get('models', getattr(self, 'models_', False))
        if not isinstance(models, (list, tuple)):
            models = [models]
        for model in models:
            if hasattr(model, 'baseDB'):  # ducktype check for collect emulator
                self._sources[model.name] = DBMongoSource(model.name, model, None)
            elif model is None:
                self._sources['__None__'] = DBNoSource('__None__', None, None)
            elif isinstance(model, str) and model[:1] == '_': # txt based one...
                self._sources[model] = DBNoSource(model, None, None)
            elif isinstance(model, DBSource):
                self._sources[model.full_name] = model
            else:
                nm = getattr(self, 'viewName_', 'view with no viewName_ set: '
                             + self.__class__.__name__)
                if model is False:
                    error = "View requires 'models_ =' class value, or 'models=' parameter, for "
                    raise TypeError(error + nm)
                else:
                    raise TypeError('Invalid type for model (within models) in '+ nm)

        self.joins_ = ObjDict()

        self.dbRows_ = self.getRows_(*args, **kwargs)

        if not isinstance(self.dbRows_, list):
            #handle legacy, single source returning raw data from mongo find
            row = self.row_name_
            self.dbRows_ = [ObjDict(((row, res), )) for res in self.dbRows_]
        
        self._source_list = list(self._sources.keys())

        if True: # self.dbRows_:
            self.changes_=[ObjDict() for r in self.dbRows_]
            if not self._baseFields:
                #print('setfields',self.viewName_)
                self.buildBaseFields_()
            self.pag_fields_ = PageDict(self,self._baseFields)
        else:
            self.changes_= []
            self.fields_=ODict()
        #self.idx_ = 0

        # auto add an entry to empty NoSource Views
        if (self.dbRows_ == [] and 
            len(self._sources) == 1 and 
            isinstance(self.default_source_, DBNoSource) ):
                self.insert_()


    @property
    def dbRowSrc_(self):
        return self.default_source_.row_source

    @dbRowSrc_.setter
    def dbRowSrc_(self, value):
        assert False,("using dbRowSrc to set values is deprecated: " +
                      self.__class__.__name__) 
        if isinstance(value,str) and value[:1] =='_':
            #local data begins with _ 
            self._sources[value] = DBSource(value, None, None)

        elif not value is None:
            self._sources[value.name] = DBSource(value.name, value, None)

    @property
    def default_source_(self):
        return list(self._sources.values())[0]

    @property
    def row_name_(self):
        """return name of first(and most often only) source """
        return self.default_source_.full_name

    @property
    def joins_(self):
        raise ValueError('obsolete use of join')
        return self._joins

    @joins_.setter
    def joins_(self,value):
        if value != ObjDict():
            raise ValueError('obselete set of join')
        self._joins = value
        for k,v in value.items():
            if not k in self._sources:
                self._sources[k] = DBSource(k, None, None)
            self._sources[k].loader = value[k]


    @property
    def idx_(self):
        return 0 #raise "do not use!"

    @property
    def view_(self):
        return self

    @property
    def fields_(self):
        """asking for fields on ViewModel itself work for a row 0"""
        return ViewRow(self,0).fields_


    @property
    def joinkeys_(self):
        return list(self.joins_.keys())

    def set_source_idx_(self, source, idxrow):
        """ records a source of data as being from a fixed record
        this is relevant when a table within a record is the source of data
        source is which source of data(key, not number)
        idxrow is the row containing the _id
        """
        self._sources[source].row_id = idxrow['_id']

    def getJoin_(self,collectName,findFilt,idx_):
        if viewModelDB is None:
            raise ViewModelError('no db')
        collect=viewModelDB.baseDB.db.get_collection(collectName)
        result=collect.find(findFilt)
        result = [ObjDict(res) for res in result]
        assert len(result)==1,'Error with find for ()join'.format(collectName)
        self.dbRows_[idx_][collectName]=result[0]

    #def __getattr__(self,name):
    #    return getattr(self.field,name)

    # @staticmethod
    def maptbl_(self, tbl):
        newrettbl = self._sources[tbl].row_source
        tblcore = tbl.split('.', 1)[0]
        oldrettbl = viewModelDB.baseDB.db.get_collection(tblcore)
        
        assert newrettbl == oldrettbl, "oops setup fail for source"
        return oldrettbl

    def update_(self):

  
        # note - could create more changes with join ids - while changes? 
        for idx_,changes in enumerate(self.changes_):
            #if not self.joins_:
            #    changes = ObjDict(table=changes)
            for tbl,change in changes.items():

                if change:
                    self._sources[tbl].save_change(self, idx_, change, tbl)
                    '''
                    src = self.maptbl_(tbl) #if self.joins_ else self.dbRowSrc_ 
                    rawrow = self.dbRows_[idx_]
                    row = rawrow[tbl] #if self.joins_ else rawrow
                    row_id = row.get('_id',self._sources[tbl].row_id)
                    if row_id is None and row:
                        pass #import pdb; pdb.set_trace()
                    if row_id is None: # or new row of []
                        # row , must be new data so inser !!  (was no _id, so should be an insert!)
                        u=src.insert(change)
                        check_error(u)
                        if '_id' in change:
                            new_id = change['_id']
                            self.dbRows_[idx_][tbl]['_id'] = new_id
                            for join_link in self._sources[tbl].join_links:
                                ins_id = new_id
                                if '.' in join_link:
                                    join_link,fld = join_link.split('.')
                                    tmpobj = self[idx_][join_link].value
                                    tmpobj[fld] = new_id
                                    ins_id = tmpobj

                                self[idx_][join_link].value = ins_id
                        #add id to this rec.... 
                        # follow join instructions (from _sources)
                    else:
                        update={'$set': re_key(tbl, idx_, change)}
                        filter_=dict(_id=row_id)
                        u=src.update_one(filter_,update)
                        check_error(u)
                '''
                changes[tbl] =  ObjDict() # see VIEW-40 about possible change 

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.update_()

    def buildBaseFields_(self ):
        """ called once for the class """

        fields=BaseFieldDict()
        #fields.__call__ = self.loop
        self.__class__._baseFields = fields
        #self.rows =self.getRow()
        cls=self.__class__
        holder=[]
        for thiscls in [cls] + cls.mro()[:-2]: #skip object and baseView
            for attribName in list(thiscls.__dict__):
                #if at in self.__dict#    at = getattr(cls,a)

                if isinstance(thiscls.__dict__[attribName],BaseField):
                    attribObj = thiscls.__dict__[attribName]
                    theRow = self.dbRows_[0] if self.dbRows_ else ObjDict()
                    name = attribObj.setup(attribName,theRow,self)
                    holder.append( (attribObj.instanceNum,attribName,attribObj))
        for num,key,obj in sorted(holder):
            #print('hkey',key)
            fields[key]= obj

        #need to set main,head,foot - but as properties of fields_ in the end!
        #print('hold',holder)
        #print('sholder',sorted(holder))
    def insert_(self):
        """ add a new blank row to the end of data
        """
        last=len(self.dbRows_)
        newrow = ObjDict()
        for k in self._sources:
            newrow[k] =ObjDict()
            if '.' in k: # insert row is inside a document
                lead,end = k.split('.',1)
                #source = self._sources[k]
                self.maptbl_(k).update(
                    {'_id': self._sources[k].row_id},
                    {'$push':{ end:{}} }
                    )
        self.dbRows_+=[newrow]
        self.changes_+=[ObjDict()]

        row = self[last]
        # for fldk in row.fields_  removed as required by VIEW-71:
        #     fld = row.fields_[fldk]
        #     if fld._default is not None:
        #         fld.value = fld._default
        return row

    def __len__(self):
        return len(self.dbRows_)

    def loop_(self,section=Section.all,case=Case.viewAll ):

        group = [self.fields,self.head,self.main.self.foot][section]
        for field in group:
            if field.cases is None or case in field.cases:
                yield field

    def __iter__(self):
        return self.fields_.loopRows()

    def getRows_(self,*args,**kwargs):
        """ overwrite getRows to retrieve rows from db within the views of
        db typical from the application
        default 'getrows' is to assume args0 is a dictionary and simply
        take args[0] as dict to find within modelName_
         note: view can have no rows at all

         two types of result are permitted for getRows_ methods
         either a list of ObjDicts - where each dict is itself a dictionary
         of fields from each source,  or for a 'single source' view, the raw
         result of a find will be converted to the list of dictionaries by the 
         calling init method.
        """
        model= self.dbRowSrc_
        if model and args:
            find = args[0]
            if not isinstance(find,dict):
                find= {}
            return model.find(find)
        else:

            return [] if not args else args[0]

    # def setRow_(self, value, condition=True):
    #     if condition:
    #         self.idx_ = value

    def __json__(self, internal=False):
        res = dict(ViewModel=self.__class__.__name__)
        if not internal:
            res=str(res)
        return res

    def labelsList_(self):
        """ list of the labelfields from dbRows
        """
        # print([ getattr(row,self.rowLabel) for row in self.dbrows])
        try:
            return [getattr(row, self.rowLabel_) for row in self.fields_.loopRows()]
        except AttributeError:
            return ['no labels' for row in self.dbRows_]

    def __getitem__(self,idx):
        return ViewRow(self,idx)

    def deprecmkList(self, rows=None, pageName=None):
        """ replacement for listTbl -expects mako to format
        handles returning whole row, but also used to give list of labels.
        this version only handles list of labels
        """
        if not rows:
            rows = self.fetchAll(**self.mapRowSpec())  # do a

        def arow(n, row):
            return n, pageName, ','.join([row[listField] for listField in self.listFields])

        return [arow(n, row) for n, row in enumerate(rows)]
