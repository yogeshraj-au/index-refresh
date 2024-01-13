from opensearchpy import OpenSearch
import os

def login_opensearch(username, password, opensearch_url):
    # Connect to OpenSearch
    opensearch_client = OpenSearch(
        hosts=[opensearch_url],
        http_auth=(username, password),
        use_ssl=True,
        verify_certs=False
    )

    # Check if the connection is successful
    if opensearch_client.ping():
        print("Connected to OpenSearch.")
        return opensearch_client
    else:
        print("Connection to OpenSearch failed.")
        return None

def get_index_patterns(opensearch_client):
    try:
        # Send a request to get the list of index patterns
        response = opensearch_client.indices.get("*")

        # Extract index patterns from the response
        index_patterns = list(response.keys())

        return index_patterns
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def refresh_index_patterns(opensearch_client, index_patterns):
    for pattern in index_patterns:
        try:
            # Send a request to refresh the specific index pattern
            opensearch_client.indices.refresh(index=pattern)
            print(f"Index pattern '{pattern}' refreshed.")
        except Exception as e:
            print(f"Error refreshing index pattern '{pattern}': {e}")
            # Handle the error as needed (e.g., log it or take corrective action)

# Example usage
opensearch_username = os.environ.get("username")
opensearch_password = os.environ.get("password")
opensearch_url = os.environ.get("url")

opensearch_client = login_opensearch(opensearch_username, opensearch_password, opensearch_url)

if opensearch_client:
    index_patterns = get_index_patterns(opensearch_client)
    
    if index_patterns:
        print("Refreshing index patterns:")
        refresh_index_patterns(opensearch_client, index_patterns)
    else:
        print("Failed to retrieve index patterns.")
