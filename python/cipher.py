import ssl

context = ssl.create_default_context()
ca_bin = context.get_ca_certs(True)

for ca in context.get_ca_certs():
    [print(k, '=', v) for k, v in ca.items()]

[print(k, '=', v) for k, v in context.session_stats().items()]
