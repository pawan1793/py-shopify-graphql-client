from py_shopify_graphql import GraphqlService
from examples.config import SHOP_DOMAIN, ACCESS_TOKEN
client = GraphqlService(SHOP_DOMAIN, ACCESS_TOKEN)

query = """
{
  shop {
    name
  }
}
"""

try:
    response = client.graphql_query_thalia(query)
    print(response)
except Exception as e:
    print("GraphQL request failed:", e)