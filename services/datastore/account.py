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
            raise Exception("username or password incorrect")
    except Exception as e:
        return None, e