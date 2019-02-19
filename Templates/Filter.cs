using DBHelper;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Backend.Model.Filter
{
    public class {name}Filter : IFilter
    {
        [NotMapped]
        public int Page { get; set; } = 1;
        [NotMapped]
        public int PerPage { get; set; } = 25;
        [NotMapped]
        public bool SortAscending { get; set; }
        [NotMapped]
        public string OrderBy { get; set; }
    }
}
