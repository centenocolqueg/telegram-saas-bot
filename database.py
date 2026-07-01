# 💾 Base de datos simple en memoria (versión inicial)

usuarios = {}

# 🧠 Crear usuario si no existe
def get_user(user_id: int):
    if user_id not in usuarios:
        usuarios[user_id] = {
            "activo": False,
            "plan": "gratis"
        }
    return usuarios[user_id]

# 🔓 Activar usuario después de pago
def activate_user(user_id: int, plan: str = "basico"):
    user = get_user(user_id)
    user["activo"] = True
    user["plan"] = plan
    usuarios[user_id] = user
    return user

# 🔒 Verificar acceso
def has_access(user_id: int):
    user = get_user(user_id)
    return user["activo"]

# 📊 Obtener plan
def get_plan(user_id: int):
    user = get_user(user_id)
    return user["plan"]
