def login (conn, username:str, password:str):
    try:
        cur = conn.cursor()
        query = '''
            select username, password 
            from public.users_web
            where username = '{0}' and password = '{1}'
        '''.format(username, password)
        cur.execute(query)
        resdata = cur.fetchone()
        if resdata:
            return resdata, None
        else:
            raise Exception("username atau password salah")
    except Exception as e:
        return None, e
    
def register_user(conn, name, username, password):
    try:
        cur = conn.cursor()
        query = '''
            INSERT INTO public.users_web (name, username, password) VALUES (%s, %s, %s)
        '''
        cur.execute(query, (name, username, password))
        conn.commit()
        return "Registration successful", None
    except Exception as e:
        conn.rollback()
        return None, e

def validate_username(conn, username):
    try:
        cur = conn.cursor()
        query = '''
                SELECT username
                FROM users_web '''
        cur.execute(query, (username))
        conn.commit()
        return "Username sudah dipakai", None
    except Exception as e:
        conn.rollback()
        return None, e
