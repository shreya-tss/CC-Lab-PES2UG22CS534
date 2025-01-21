# from locust import task, run_single_user, FastHttpUser

# class Browse(FastHttpUser):
#     host = "http://localhost:5000"

#     # Inline request headers to avoid unnecessary setup
#     @task
#     def browse_task(self):
#         """Simulates a user browsing with minimal overhead."""
#         headers = {
#             "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
#             "Host": "localhost:5000",
#             "Priority": "u=0, i",
#             "Sec-Fetch-Dest": "document",
#             "Sec-Fetch-Mode": "navigate",
#             "Sec-Fetch-Site": "cross-site",
#             "Upgrade-Insecure-Requests": "1",
#         }

#         # Directly handle the response without using catch_response unless needed for detailed checks
#         resp = self.client.get("/browse", headers=headers)
#         if resp.status_code == 200:
#             return  # If successful, simply return without explicit success
#         else:
#             # Log failure for failed requests
#             print(f"Request failed with status code {resp.status_code}")

# if __name__ == "__main__":
#     run_single_user(Browse)



from locust import task, run_single_user
from locust import FastHttpUser


class browse(FastHttpUser):
    host = "http://localhost:5000"
    default_headers = {
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "DNT": "1",
        "Sec-GPC": "1",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
    }

    @task
    def t(self):
        with self.client.request(
            "GET",
            "/browse",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
                "Host": "localhost:5000",
                "Priority": "u=0, i",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "cross-site",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
       

if __name__ == "__main__":
    run_single_user(browse)
