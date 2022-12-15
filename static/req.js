$('#get_b').on('click', function () {
    let post_id = $('#get_num').val()
    $.ajax({
        url: 'https://jsonplaceholder.typicode.com/posts/' + post_id,
        method: 'GET',
        contentType: "application/json",
        success: function (response) {
            console.log('success GET')
            $('#to_get').text('Содержание поста: ' + response.body)
        },
        error: function (response) {
            $('#to_get').text('Ошибка, поста с таким ID не существует')
        }
    })
})

$('#post_b').on('click', function () {
    let post_body = $('#post_body').val()
    $.ajax({
        url: 'https://jsonplaceholder.typicode.com/posts',
        method: 'POST',
        data: JSON.stringify({
            'body': post_body
        }),
        contentType: "application/json",
        success: function (response) {
            console.log('success POST')
            $('#to_post').text('ID созданного поста: ' + response.id)
        },
        error: function (response) {
            $('#to_post').text('Ошибка, поста с таким ID не существует')
        }
    })
})

$('#put_b').on('click', function () {
    let put_body = $('#put_body').val()
    let put_num = $('#put_num').val()
    $.ajax({
        url: 'https://jsonplaceholder.typicode.com/posts/' + put_num,
        method: 'PUT',
        data: JSON.stringify({
            'body': put_body
        }),
        contentType: "application/json",
        success: function (response) {
            console.log('success PUT')
            $('#to_put').text('Успешно для ID: ' + response.id)
        },
        error: function (response) {
            $('#to_put').text('Ошибка, поста с таким ID не существует')
        }
    })
})
