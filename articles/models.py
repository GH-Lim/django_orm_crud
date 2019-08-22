from django.db import models

# 1. python manage.py makemigrations => django 한테 model 작성했음을 알림
# 2. python manage.py migrate => django 한테 실제 DB 에 작성하라고 명령

# Create your models here.
# 얘는 단수형으로 만듭니다.
class Article(models.Model): # 장고 Model을 상속 받습니다.
    # id(pk) 는 기본적으로 처음 테이블 생성시 자동으로 만들어 진다.
    # id = models.AutoField(primary_key=True)  # 자동으로 아이디 번호를 매겨줍니다.

    # 모든 필드는 기본적으로 NOT NULL => 비어있으면 안된다.

    # 게시판을 만들자
    # CharField 에서는 max_lenth 가 필수 인자다.
    title = models.CharField(max_length=20)  # 클래스 변수 (DB 의 필드(column))
    content = models.TextField() # 클래스 변수 (DB 의 필드) 엄청 긴 변수
    created_at = models.DateTimeField(auto_now_add=True) # 데이터가 추가됐을때 자동으로
    updated_at = models.DateTimeField(auto_now=True) # 언제든지 자동으로 (수정됐을때도)

    # 1 모델 작성
    # 2 메이크migrations
    # 3 migrate
    def __str__(self):
        return f'{self.id}번 글 - {self.title} : {self.content}'
