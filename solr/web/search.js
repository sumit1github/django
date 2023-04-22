function redirect(element){
    var url = element.getAttribute('url')
    location.href = url;
}


function range_search(el, target_id) {

  var filter_by = el.getAttribute('filter_by');
  if (filter_by == 'price') {
    var min = document.getElementById('price_min').value;
    var max = document.getElementById('price_max').value;

    var query = '[' + min + ' TO ' + max + ']';

    var target = document.getElementById(target_id);
    target.setAttribute('query', query);
  } else if (filter_by === 'creepage_distance') {

    var min = document.getElementById('creepage_min').value;
    var max = document.getElementById('creepage_max').value;

    var query = '[' + min + ' TO ' + max + ']';
    var target = document.getElementById(target_id);
    target.setAttribute('query', query);
  }
  else if (filter_by === 'voltage') {

    var min = document.getElementById('voltage_min').value;
    var max = document.getElementById('voltage_max').value;

    var query = '[' + min + ' TO ' + max + ']';
    var target = document.getElementById(target_id);
    target.setAttribute('query', query);
  }
  else if (filter_by === 'insulation_diameter') {

    var min = document.getElementById('insulation_diameter_min').value;
    var max = document.getElementById('insulation_diameter_max').value;

    var query = '[' + min + ' TO ' + max + ']';
    var target = document.getElementById(target_id);
    target.setAttribute('query', query);
  }
  else if (filter_by === 'shed_inside_diameter') {

    var min = document.getElementById('shed_inside_diameter_min').value;
    var max = document.getElementById('shed_inside_diameter_max').value;

    var query = '[' + min + ' TO ' + max + ']';
    var target = document.getElementById(target_id);
    target.setAttribute('query', query);
  }

  else if (filter_by === 'sheath_ouside_diameter') {

    var min = document.getElementById('sheath_ouside_diameter_min').value;
    var max = document.getElementById('sheath_ouside_diameter_max').value;

    var query = '[' + min + ' TO ' + max + ']';
    var target = document.getElementById(target_id);
    target.setAttribute('query', query);
  }

  else if (filter_by === 'termination_length') {

    var min = document.getElementById('termination_length_min').value;
    var max = document.getElementById('termination_length_max').value;

    var query = '[' + min + ' TO ' + max + ']';
    var target = document.getElementById(target_id);
    target.setAttribute('query', query);
  }
  else if (filter_by === 'install_length_butt') {

    var min = document.getElementById('install_length_butt_min').value;
    var max = document.getElementById('install_length_butt_max').value;

    var query = '[' + min + ' TO ' + max + ']';
    var target = document.getElementById(target_id);
    target.setAttribute('query', query);
  }
  else if (filter_by === 'conductor_diameter') {

    var min = document.getElementById('conductor_diameter_butt_min').value;
    var max = document.getElementById('conductor_diameter_butt_max').value;

    var query = '[' + min + ' TO ' + max + ']';
    var target = document.getElementById(target_id);
    target.setAttribute('query', query);
  }
}



function product_list(product_list) {
  var unique_list = [...new Set(product_list)];

  target = document.getElementById('product_list');
  target.innerHTML = '';
  console.log(product_list)

  for (var product = 0; product < unique_list.length; product++) {

    // image url
    if (unique_list[product]['image'][0] === '') {
      var image = ''
    } else {
      var image = unique_list[product]['image'][0]
    }

    // product details url 
    var product_detail_url = "{% url 'app1_product_master:product_detail' 0 %}".replace("0", unique_list[product][
      'id'
    ][0]);

    html = '\
    <div class="col-xs-6 col-md-3 mt-4">\
      <div class="card" style="width:17rem;">\
        <div class="image-container">\
          <img src="'+image+'" class="product_image" alt="...">\
        </div>\
        <div class="card-body">\
          <h5 class="card-title">'+unique_list[product]['name'][0]+'</h5>\
          <p class="text">Filter</p>\
          <div class="content">\
            <div>\
              <p class="card-text mb-0">$ '+unique_list[product]['price'][0]+'</p>\
              <span>'+unique_list[product]['voltage'][0]+' kv</span>\
            </div>\
            <a href="#" class="btn">Add to Cart</a>\
          </div>\
        </div>\
        <p class="rate"> id : '+ unique_list[product]['id']+'</p>\
      </div>\
    </div>\
    '
    target.innerHTML += html;
  };

}


function termination_search(htmle) {
  var filter_by = htmle.getAttribute("filter_by");
  var query = htmle.getAttribute("query");

  var query_string = filter_by + '=' + encodeURIComponent(query) + '&';

  document.getElementById('query_holder').value += query_string;

  var search_query_string = document.getElementById('query_holder').value;

  console.log(search_query_string);

  var search_url = '/product/termination_product_search/?' + search_query_string;
  console.log(search_url);
  axios.get(search_url)
    .then(function (response) {
        
      product_list(response.data);
    })
    .catch(function (error) {
      // handle error
      console.log(error);
    })

}



