# Django ORM

## Create

## 기초 설정

- Shell

  ```bash
  $ python manage.py shell
  ```

- import model

  ```python
  >>> from articles.models import Article
  ```

  ```python
  >>> Article.object.all()
  <QuerySet []>
  ```

  Article 은 우리가 만든 model

  object는 db에 접근해서 명령을 내리게 하는 객체

### 데이터를 저장하는 3가지 방법

1. 첫번째 방식

   - ORM 을 쓰는 이유는?

     DB 를 조작하는 것을 객체지향 프로그래밍 (클래스) 처럼 하기 위해서

     ```python
     >>> article = Article()
     >>> article
     <Article: Article object (None)>
     >>> article.title = 'First article'
     >>> article.content = 'Hello article?'
     >>> article.title
     'First article'
     >>> article.content
     'Hello article?'
     >>> article.save() # 저장한다!
     >>> article
     <Article: Article object (1)> # id 값이 생성되면서 id 값이 보여짐
     >>> Article.objects.all()
     <QuerySet [<Article: Article object (1)>]>
     ```

     `ctrl + shift + p` => `SQlite: Open Database` 를 통해 확인해보면 excel sheet 처럼 나오는 것을 확인할 수 있음

2. 두번째 방식

   - 함수에서 keyword 인자 넘기기 방식과 동일

     ```python
     >>> article = Article(title='Second article', content='Hi second')
     >>> article.save()
     >>> article
     <Article: Article object (2)>
     >>> Article.objects.all()
     <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>]>
     ```

3. 세번째 방식

   - `create` 를 사용하면 `QuerySet` 객체를 생성하고 저장하는 로직이 한번의 스텝으로 가능

     ```python
     >>> Article.objects.create(title='Third', content='Django! Good!')
     <Article: Article object (3)>
     >>> Article.objects.all()
     <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>]>
     ```

### 올바른 입력인지 검증

`article.full_clean()` 을 사용

```python
>>> article = Article()
>>> article.title = 'Python is good'
>>> article.full_clean()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "C:\Users\student\development\django\django_orm_crud\venv\lib\site-packages\django\db\models\base.py", line 1203, in full_clean
    raise ValidationError(errors)
django.core.exceptions.ValidationError: {'content': ['이 필드는 빈 칸으로 둘 수 없습니다.']}
```

## Read

```python
>>> Article.objects.all()
<QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>]>
```

#### 객체 표현 변경

- `models.py` - `class Article(models.Model)`에 추가

  ```python
  def __str__(self):
      return f'{self.id}번 글 - {self.title} : {self.content}'
  ```

- 모든 객체

  ```python
  >>> from articles.models import Article
  >>> Article.objects.all()
  <QuerySet [<Article: 1번 글 - First article : Hello article?>, <Article: 2번 글 - Second article : Hi second>, <Article: 3번 글 - Third : Django! Good!>]>
  ```

- DB 에 저장된 글 중에서 title이 Second 인 글만 가져오기

  ```python
  >>> Article.objects.filter(title='Second article')
  <QuerySet [<Article: 2번 글 - Second article : Hi second>]>
  >>> Article.objects.filter(title='Second article')
  <QuerySet [<Article: 2번 글 - Second article : Hi second>, <Article: 4번 글 - Second article : second second>]>
  ```

- DB에 저장된 글 중에서 title이 Second 인 글 중 첫번째만 가져오기

  ```python
  >>> querySet = Article.objects.filter(title='Second article')
  >>> querySet
  <QuerySet [<Article: 2번 글 - Second article : Hi second>, <Article: 4번 글 - Second article : second second>]>
  >>> querySet.first()
  <Article: 2번 글 - Second article : Hi second>
  
  >>> Article.objects.filter(title='Second article').first()
  <Article: 2번 글 - Second article : Hi second>
  ```

- DB에 저장된 글 중에서 pk가 1인 글만 가지고 오기

  ```python
  >>> Article.objects.get(pk=1)
  <Article: 1번 글 - First article : Hello article?>
  ```

  get 으로 접근은 무조건 값이 하나(unique 한 값)라고 확신하는 값으로 가져온다. 일반적으로 pk

  없는 값이나 중복되는 값을 꺼내려고 하면 에러가 발생한다.

  filter는 없는 값을 불러와도 에러는 안뜨지만 빈 `QuerySet`을 반환한다.

- 오름차순

  ```python
  >>> articles = Article.objects.order_by('pk')
  >>> articles
  <QuerySet [<Article: 1번 글 - First article : Hello article?>, <Article: 2번 글 - Second article : Hi second>, <Article: 3번 글 - Third : Django! Good!>, <Article: 4번 글 - Second article : second second>]>
  ```

- 내림차순

  ```python
  >>> articles = Article.objects.order_by('-pk')
  >>> articles
  <QuerySet [<Article: 4번 글 - Second article : second second>, <Article: 3번 글 - Third : Django! Good!>,
  <Article: 2번 글 - Second article : Hi second>, <Article: 1번 글 - First article : Hello article?>]>
  ```

- 인덱스 접근이 가능하다

  ```python
  >>> article = articles[2]
  >>> article
  <Article: 2번 글 - Second article : Hi second>
  >>> articles = Article.objects.all()[1:3]
  >>> articles
  <QuerySet [<Article: 2번 글 - Second article : Hi second>, <Article: 3번 글 - Third : Django! Good!>]>
  ```

- LIKE - 문자열을 포함하고있는 값을 가지고 온다

  장고 ORM 은 이름과 필터를 더블언더스코어(__)로 구분한다.

  ```python
  >>> articles = Article.objects.filter(title__contains='Sec')
  >>> articles
  <QuerySet [<Article: 2번 글 - Second article : Hi second>, <Article: 4번 글 - Second article : second second>]>
  ```

- `startswith`

  ```python
  >>> articles = Article.objects.filter(title__startswith='first')
  >>> articles
  <QuerySet [<Article: 1번 글 - First article : Hello article?>]>
  ```

- `endswith`

  ```python
  >>> articles = Article.objects.filter(content__endswith='good!')
  >>> articles
  <QuerySet [<Article: 3번 글 - Third : Django! Good!>]>
  >>> articles[0] # 인덱스 접근 역시 가능
  <Article: 3번 글 - Third : Django! Good!>
  ```

## Delete

article 인스턴스 호출 후 `.delete()`

```python
>>> article = Article.objects.get(pk=1)
>>> article
<Article: 1번 글 - First article : Hello article?>
>>> article.delete()
(1, {'articles.Article': 1})
```

## Update

article 인스턴스 호출 후 값 변경하여 `.save()`

```python
>>> article = Article.objects.get(pk=4)
>>> article.content
'second second'
>>> article.content = 'new content'
>>> article.save()
>>> article.content
'new content'
```

