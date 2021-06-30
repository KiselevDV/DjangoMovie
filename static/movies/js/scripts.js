// Функция принимает url = {% url 'movies:json_filter' %} и params (жанры/года)
function ajaxSend(url, params) {
    // Отправляем запрос с помощью fetch (сам AJAX). Выстраиваем объект и получаем промисы
    fetch(`${url}?${params}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
    })
        // Превый промис преобразует ответ в JSON
        .then(response => response.json())
        // Отправить JSON в ф-ию render
        .then(json => render(json))
        // Если произошла ошибка вывести её в консоль
        .catch(error => console.error(error))
}

// // START
// // Поиск формы по имени - name="filter"
// const forms = document.querySelector('form[name=filter]');
// // Когда у неё, будет вызван метод submit - выполнится ф-ия
// forms.addEventListener('submit', function (e) {
//     // Получаем данные из формы
//     e.preventDefault();  // убрать стандартное поведение 'submit'
//     // получить информацию из атрибута action (формы) - {% url 'movies:json_filter' %}
//     let url = this.action;
//     // URLSearchParams - выстраивает параметры для передачи, получает данную форму 'this'
//     // с помощью FormData и всё преобразует (через toString) в строку => params (жанры/года)
//     let params = new URLSearchParams(new FormData(this)).toString();
//     ajaxSend(url, params);
// });

// Принимает ответ в виде JSON, data = response.json()
function render(data) {
    // Рендер шаблона
    // С помощью библиотеки hogan.js компилируем HTML
    let template = Hogan.compile(html);
    // Отрендерить часть шаблона (html) данными с сервера (response.json())
    let output = template.render(data);

    // Найти данный див в шаблоне
    const div = document.querySelector('.left-ads-display>.row');
    // Вставить в него данные
    div.innerHTML = output;
}

// HTML из movie_list, для рендера фильма
let html = '\
{{#movies}}\
    <div class="col-md-4 product-men">\
        <div class="product-shoe-info editContent text-center mt-lg-4">\
            <div class="men-thumb-item">\
                <img src="media/{{ poster }}" class="img-fluid" alt="">\
            </div>\
            <div class="item-info-product">\
                <h4 class="">\
                    <a href="/{{ url }}" class="editContent">{{ title }}</a>\
                </h4>\
                <div class="product_price">\
                    <div class="grid-price">\
                        <span class="money editContent">{{ tagline }}</span>\
                    </div>\
                </div>\
                <ul class="stars">\
                    <li><a href="#"><span class="fa fa-star" aria-hidden="true"></span></a></li>\
                    <li><a href="#"><span class="fa fa-star" aria-hidden="true"></span></a></li>\
                    <li><a href="#"><span class="fa fa-star-half-o" aria-hidden="true"></span></a></li>\
                    <li><a href="#"><span class="fa fa-star-half-o" aria-hidden="true"></span></a></li>\
                    <li><a href="#"><span class="fa fa-star-o" aria-hidden="true"></span></a></li>\
                </ul>\
            </div>\
        </div>\
    </div>\
{{/movies}}'


// Add star rating
// Поиск нужной формы
const rating = document.querySelector('form[name=rating]');
// Когда у формы вызовется событие 'change'
rating.addEventListener("change", function (e) {
    // При создании новой формы получим все значения полей в data
    let data = new FormData(this);
    // С помощью fetch, на url формы ${this.action} отправляем POST запрос
    fetch(`${this.action}`, {
        method: 'POST',
        body: data  // передача в body данные из формы
    })
        .then(response => alert("Рейтинг установлен"))
        .catch(error => alert("Ошибка"))
});