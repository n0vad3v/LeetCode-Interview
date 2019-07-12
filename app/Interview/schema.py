import graphene

import search.schema

class Query(search.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
