using API.Response;
using System;
using Backend.Business;
using System.Web.Http;
using Backend.Model.Filter;
using Backend.Model;

namespace API.Controllers
{
    public class {name}Controller: BaseController
    {
        private {name}Business business;
        private {name}Response response;

        public {name}Controller()
        {
            business = new {name}Business();
            response = new {name}Response();
        }


        // GET: api/{name}/5
        [HttpGet]
        public IHttpActionResult Get(long id)
        {
            try
            {
                response.{name} = business.Get(id);
            }
            catch (Exception ex)
            {
                response.Success = false;
                response.Message = ex.Message;
            }

            return Ok(response);
        }

        [HttpGet]
        public IHttpActionResult List([FromUri] {name}Filter filter)
        {
            try
            {
                response.List = business.List(filter);
            }
            catch (Exception ex)
            {
                response.Success = false;
                response.Message = ex.Message;
            }

            return Ok(response);
        }

        // POST: api/{name}
        [HttpPost]
        public IHttpActionResult Create({name} {nameLower})
        {
            try
            {
                business.Save({nameLower});
            }
            catch (Exception ex)
            {
                response.Success = false;
                response.Message = ex.Message;
            }

            return Ok(response);
        }

        // PUT: api/{name}
        [HttpPut]
        public IHttpActionResult Update({name} user)
        {
            try
            {
                business.Update(user);

            }
            catch (Exception ex)
            {
                response.Success = false;
                response.Message = ex.Message;
            }

            return Ok(response);
        }


        // DELETE: api/{name}/5
        [HttpDelete]
        public IHttpActionResult Delete(int id)
        {
            try
            {
                business.Delete(id);
            }
            catch (Exception ex)
            {
                response.Success = false;
                response.Message = ex.Message;
            }
            return Ok(response);
        }
    }
}