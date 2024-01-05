class Data_Holder():
    def __init__(self, prop_list,branch, data, source, source_folder):
        self.data = data
        self.branch = branch  
        self.prop_list = prop_list
        self.source_folder = source_folder
        self.source = source



class Prop_Holder():
    def __init__(self, pset, prop, group):
        self.pset = pset
        self.prop = prop
        self.group = group
    
def filterConfig(_cat_name, _conf_lst):
    try:
        search_res = [x for x in _conf_lst if x.branch == _cat_name][0]

    except:
        search_res = None
    return search_res
