# from flask import Flask

# app = Flask(__name__)

# try:
#     from controller import user_controller

# except Exception as e:
#     print(e)

# print(app.url_map)

from flask import Flask
print("APP.PY __name__ =", __name__)
app = Flask(__name__)

import traceback

try:
    from controller import user_controller
    print("APP ID IN APP.PY =", id(app))
except Exception:
    traceback.print_exc()

print(app.url_map)

if __name__ == "__main__":
    app.run(debug=True)