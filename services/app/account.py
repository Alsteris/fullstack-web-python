from pkg import openConnection
import datastore

# import function datasore

def login(username: str, password: str):
    try:
        conn, err = openConnection()
        if err != None or conn == None:
            raise Exception(f"{err}")
        
        resLogin, err = datastore.login(conn, username, password)
        if err != None:
            raise Exception(err)
        return resLogin, None
    except Exception as e:
        return None, e
            
def register(name, username, password):
    try:
        conn, err = openConnection()
        if err != None or conn == None:
            raise Exception(f"{err}")
        
        resValidate, err = datastore.validate_username(conn, username)
        if resValidate not in (None,{}):
                raise Exception("Username sudah dipakai!")
        
        resRegister, err = datastore.register_user(conn, name, username, password)
        if err != None:
            raise Exception(err)
        return resRegister, None
    except Exception as e:
        return None, e
    
