import requests

def get_api_response(query):
    endpoint = 'https://api.mininxd.my.id/gemini'

    try:
        response = requests.get(f"{endpoint}?q={query}", headers={'Accept': 'application/json'})

        # Periksa apakah respons berhasil
        if response.status_code != 200:
            raise Exception(f"HTTP error! Status: {response.status_code}")

        # Konversi respons ke JSON
        data = response.json()
        return data
    except Exception as e:
        print('Error:', e)
        return None

def main():
    # Contoh prompt untuk pengguna
    print("API Query Program")
    print("==================")
    query = input("Masukkan query Anda: ")

    # Mendapatkan respons dari API
    response = get_api_response(query)

    if response is not None:
        # Tampilkan hanya bagian 'text' dari respons
        print("Response dari API:")
        if 'text' in response:
            print(response['text'])
        else:
            print("Tidak ada 'text' dalam respons.")
    else:
        print("Gagal mendapatkan respons dari API.")

if __name__ == "__main__":
    main()
