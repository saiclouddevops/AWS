

Object = {"a":{"b":{"c":"d"}}}
key = "a/b/c"

def json_Object(obj, key):
    arr = []
    
    count=0
    keys=key.split("/")
    def search(obj, arr, key, count):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    if(k == keys[count]):
                        count+=1
                        search(v, arr, key,count)
                elif(k == keys[count]):
                    arr.append(v)

        return arr

    values = search(obj, arr, key, count)
    return values

print(json_Object(Object,key))