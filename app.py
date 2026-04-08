import fastapi_poe as fp

message = fp.ProtocolMessage(
    role = "user",
    content = "Hello world"
)

api_key = "sk-poe-k7GRYbms63Kf9m5Fzk7IP-E6os2druFPlYdbVkxKKlg"  # or os.getenv("POE_API_KEY")

for partial in fp.get_bot_response_sync(
    messages = [message],
    bot_name = "RayatAI",
    api_key = api_key
):
    print(partial)
