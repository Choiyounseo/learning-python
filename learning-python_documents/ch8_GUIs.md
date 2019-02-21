# The Edges - GUIs and Scripts

* `GUI`(graphical user interface) : a type of interface that allows the user to interact with an electronic device through graphical icons, buttons and widgets, as opposed to text-based or command-line interfaces, which require commands or text to be typed on the keyboard



* Python gives very simple HTTP server for free

* ```
  $ python -m http.server 8000
  
  $ ./serve.sh
  // 위 command를 serve.sh파일에 저장 후, serve.sh 실행도 가능
  ```

* `Base64` : binary-to-text encoding scheme that represents binary data in ASCII string format by translating it into radix-64 representation

---

### Parsing arguments

* Python `argparse` : 사용자 친화적인 명령행 인터페이스를 쉽게 작성하도록 도와줌

  * 명령행 옵션, 인자와 부속 명령을 위한 parser
  * `sys.argv`를 어떻게 파싱할지 파악

  ```python
  parser = argparse.ArgumentParser()
  
  parser.add_argument()
  
  # in order to parse all the arguments...
  args = parser.parse_args()
  ```

### The business logic

* `BeautifulSoup` library : allow us to parse a web page in no time, without having to write all the logic that would be needed to find all the images in a page

  ```python
  soup = BeautifulSoup(page.content, 'html.parser')
  
  for img in soup.findAll('img'):
          src = img.get('src')
  ```

---

### GUI application

* Python GUI libraries...
  * tkinter
  * tkinter.tix module (Tk Interface Extension)
  * turtle module
  * wxPython, PyGTK, PyQt





p.299 다시 참고! (how to improve the application)

-> flask과 합쳐서 만들어보자..