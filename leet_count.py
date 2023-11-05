import requests
import sys

def solved(username):
    api = "https://leetcode.com/graphql"
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0" 
    }
    query = {
        "query": """
        query { 
            matchedUser(username: "%s") {
                submitStatsGlobal {
                    acSubmissionNum {
                        difficulty
                        count
                        submissions
                    }
                }
            }
        }
        """ % username,
    }
    try:
        response = requests.post(api, json=query, headers=headers)
        return (response.json()
            ['data']
            ['matchedUser']
            ['submitStatsGlobal']
            ['acSubmissionNum'][0]['count']
        )
    except Exception as e:
        return None

if __name__ == '__main__':
    print(solved(sys.argv[1]))
