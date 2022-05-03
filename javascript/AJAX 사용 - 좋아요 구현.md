```
<script>
	# csrf token 사용
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

    # csrf token 정보를 axios header에 추가하기 위해 config 값을 object형태로 변경
    const csrfConfig = {
      headers: {'X-CSRFToken': csrftoken},
    }

    const likeForms = document.querySelectorAll('.like-form')

    # eventlistener 를 추가
    likeForms.forEach(form => {
      form.addEventListener('submit', function (event) {
        event.preventDefault()
        
        # pk 정보 가져오기
        const articlePk = form.dataset.articleId

        # 요청 url 만들기
        const LIKE_URL = `/articles/${articlePk}/likes/`

        # csrf 헤더 설정을 config 인자에 전달
        axios.post(LIKE_URL, null, csrfConfig)
          .then(res => {
            console.log(res.data)

            return res.data
          })

          .then(res => {
            const likeBtn = document.querySelector(`#like-${articlePk}`)
            const likeCnt = document.querySelector(`#like-count-${articlePk}`)

            if (res.liked) {
              likeBtn.innerHTML = 
              '<i class="fa-solid fa-heart" style="color:crimson;"></i>'

            }else {
              likeBtn.innerHTML = '<i class="fa-solid fa-heart"></i>'
            }
            
            likeCnt.innerHTML = res.like_cnt
          })

          .catch(err => {
            console.log(err)
          })
      })
  })
</script>
```

