from neo4j import GraphDatabase

class Neo4jConnection:
    def __init__(self, url, user, password):
        self._driver = GraphDatabase.driver(url, auth=(user, password))

    def close(self):
        self._driver.close()

    def query(self, query, parameters=None):
        session = None
        response = None
        try:
            session = self._driver.session()
            response = list(session.run(query, parameters))
        except Exception as e:
            print("ERRO no sistema", e)
        finally:
            if session:
                session.close()
        return response