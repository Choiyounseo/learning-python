# Web Development

### Web

* protocol : 컴퓨터나 원거리 통신 장비 사이에서 메세지를 주고 받는 양식과 규칙의 체계

* HTTP (Hypertext Transfer Protocol)
  * HTTP protocol : *stateless*
    * current request has no knowledge about what the illusion of being logged in
* TCP/IP (Transmission Control Protocol/Internet Protocol)
  * HTTP is based on TCP/IP, provides the tool for a reliable communication exchange

---

### Django web framework

* web framework : set of tools(libraries, functions, classes, and so on) that we can use to code a website
  * need to decide what kind of requests we want to allow to be issued against our web server and how we respond to them
  * designed around *MTV(model-template-view)* pattern, which is variant of *MVC(model-view-controller)*



**[Model Layer]**

* ORM(object-relational mapping)

  * OOP언어에서, RDBMS를 연동할 때, 클라이언트 라이브러리/SQL을 대체하여 구현가능
    * `RDBMS`
      * RDB를 생성하고, 수정하고, 관리할 수 있는 소프트웨어
    * `RDB` (relational database)
      * key와 value들의 간단한 관계를 테이블화 시킨 매우 간단한 원칙의 전산정보 데이터베이스 ( 관계형 data model에 기초를 둔 db)
      * Oracle, MySQL
      * 모든 테이블을 2차원 테이블로 표현
      * 테이블은 row(record, tuple)과 column(field, item)으로 이루어진 기본 데이터 저장 단위
      * 상호관련성을 가진 테이블의 집합

  

  * **Flask는 SQLAlchemy / Django는 내장 ORM / Node.js는 Sequalize**

  

  * 데이터 관련 OOP 프로그래밍을 쉽게 하도록 도와주는 기술
  * Model Class를 통해서 객체 형성, 이 객체를 통해 DB에 접근한다
  * objects : model manager, DB와 Django Model사이의 *Query Operation(질의연산)* 인터페이스 역할
  * objects를 사용해 다수의 데이터를 가져오는 함수를 사용할 때 반환되는 객체가 '*QuerySet*'

* Django ORM : takes care of translating operations done on Python objects into a language that a relational database can understand

  * SQL(Structured Query Language)



**[View Layer]**

* functinon of view : handling a request, performing whatever action needs to be carried out, and eventually returning a response
  * flask의 'view_function'!!
* view : mechanism through which we can fulfill a request
* response object : JSON, HTML(Hypertext Markup Language)....



**[Template Layer]**

* template layer : bride between backend and frontend development
* When a view has to return HTML, it usually does it by preparing a context object (a dict) with some data, and then it feeds this context to a **template, which is rendered (that is to say, transformed into HTML) and returned to the caller in the form of a response** (more precisely, the body of the response)

---

### Django URL dispatcher

*  URL (Uniform Resource Locator)
* The way Django associates a Uniform Resource Locator (URL) with a view is through matching the requested URL with the patterns that are registered in a special file.

---

### Regular expressions

* Regular expression(**regex**) : sequence of characters that defines a search pattern with which we can carry out operations such as pattern and string matching, find/replace, and so on
  * 특정한 규칙을 가진 문자열의 집합을 표현하는데 사용하는 형식 언어
  * 문자열의 검색과 치환을 위한 용도로 사용

* ex) two digits, one dash, two digits, one dash, four digits
  * => [0-9]{2} - [0-9]{2} - [0-9]{4}
* http://www.nextree.co.kr/p4327/
* '^' & '$' : *start* & *end* of a string

---

### Regex website

```
$ django-admin startproject regex
// will prepare the skeleton for Django project called 'regex'

$ python manage.py runserver
// 위의 command로 인해 manage.py라는 파일 생성됨
// localhost:8000 작동

$ python manage.py startapp entries

$ python manage.py migrate
// apply 'migrations' to the database

$ python manage.py createsuperuser
// create superuser
```



* migration 의 두 종류
  * Data migration
  * schema migration



python makemigrations | flask db migrate

python migrate | flask db upgrade 개념?

---

### Creating the form

* Security ( CSRF - cross-site request forgery ) attack : data is sent from a domain that is not the one the user is authenticated on
  * (사이트간 요청 위조) : 웹 어플리케이션 취약점 중 하나로, 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹페이지를 보안에 취약하게 하거나, 수정, 삭제등의 작업을 하게 만드는 공격방법

---

* Django, Flask, Falcon ( Python based frameworks )



* gunicorn의 역할?



* **orm없이 SQL사용법 알아보기.....**