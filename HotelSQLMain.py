from infraestructure import SQLiteInfraestructure
from adapters import SQLiteAdapter
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
all_users_data = None
all_users_csv_data = None
# Llamada a la función para recuperar todos los datos de dim_users
query = 'SELECT * FROM dim_users LIMIT 3;'
#SQLiteAdapter.drop_table_dim_users()
SQLiteAdapter.select(query)
#SQLiteAdapter.select_all_from_dim_csv_users(query)    