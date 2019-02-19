using Backend.DAO;
using Backend.Model;
using Backend.Model.Filter;
using DBHelper;
using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Transactions;

namespace Backend.Business
{
    public class {name}Business
    {
        private readonly {name}DAO _{nameLower}DAO;

        private TransactionOptions _option = new TransactionOptions
        {
            IsolationLevel = IsolationLevel.ReadCommitted,
            Timeout = TimeSpan.MaxValue
        };

        public {name}Business()
        {
            this._{nameLower}DAO = new {name}DAO();
        }

        public {name} Get(long id)
        {
            return this._{nameLower}DAO.Get(new SqlParameter("{name}Id", id));
        }

        public IFilterable List({name}Filter filter)
        {
            return this._{nameLower}DAO.List(filter);
        }

        public int Save({name} obj)
        {
            return this._{nameLower}DAO.Save(obj);
        }

        public void Update({name} obj)
        {
            this._{nameLower}DAO.Update(obj.{name}Id, obj);
        }

        public void Delete(int id)
        {
            this._{nameLower}DAO.Delete(id);
        }
    }
}
