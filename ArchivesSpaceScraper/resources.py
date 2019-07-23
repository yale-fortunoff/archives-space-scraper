def get_id_string(resource):

    ret = []
    
    for field in ["id_%d" % x for x in range(4)]:
        if field in resource.keys() and len(resource[field]) > 1:
            ret.append(resource[field])
            
    return "-".join(ret).strip()
