from django.db import models

# Create your models here.
# 얘는 단수형으로 만듭니다.
class Article(models.Model): # 장고 Model을 상속 받습니다.
    # id(pk) 는 기본적으로 처음 테이블 생성시 자동으로 만들어 진다.
    # id = models.AutoField(primary_key=True)  # 자동으로 아이디 번호를 매겨줍니다.

    # 게시판을 만들자
    # CharField 에서는 max_lenth 가 필수 인자다.
    title = models.CharField(max_length=20)  # 클래스 변수 (DB 의 필드(column))
    content = models.TextField() # 클래스 변수 (DB 의 필드) 엄청 긴 변수
    created_at = models.DateTimeField(auto_now_add=True)
    
