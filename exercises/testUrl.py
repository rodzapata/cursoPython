import time
import requests

def test_endpoint(url, times=100):
    start = time.time()
    for _ in range(times):
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Error {response.status_code} in {url}")
    end = time.time()
    return (end - start) / times  # tiempo promedio

spring_url = "http://localhost:8080/menus"
fastapi_url = "http://localhost:8000/menus"

spring_avg = test_endpoint(spring_url)
fastapi_avg = test_endpoint(fastapi_url)

print(f"Spring Boot promedio: {spring_avg:.4f} segundos")
print(f"FastAPI promedio: {fastapi_avg:.4f} segundos")
