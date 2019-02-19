using Backend.Model;
using DBHelper;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Backend.DAO
{
    public class {name}DAO : AbstractDAO<{name}>
    {
        public {name}DAO() : base() { }

        public {name}DAO(string connection) : base(connection) { }

        public override void Delete<K>(K id)
        {
            dbHelper.Delete<{name}, K>(id);
        }

        public override int Save({name} obj)
        {
            return dbHelper.Save(obj);
        }

        public override void Update<k>(k id, {name} obj)
        {
            dbHelper.Update(id, obj);
        }
    }
}
