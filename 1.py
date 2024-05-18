# 이 첫번째 프로젝트는 제품 구매시 자동적으로 상품을 보낼수 있도록 하는 코드 입니다.
# 이메일로 보낼수 있도록 하는 코드이며, 수신, 발신 이메일을 요구로 합니다.
# 이메일 전송할때 사용되는 프로토콜은 smtp 이며, 특히나 지메일은 보안상의 이유로 TLS 보안을 사용한다.


# 주의: :39의 코드를 실행하면 실제로 전송이 됩니다. 사용자가 실행하실때는 사용자에 맞게 전송하시길 바랍니다.





import smtplib

from email.mime.text import MIMEText


# 세션을 s 로 설정, gmail을 통해서 보낸다. 포트는 587
s = smtplib.SMTP('smtp.gmail.com', 587)

# TLS 보안 시작(보안 상의 이유로 지메일은 TLS 모드를 사용함.)
# TLS: 전송 계층 보안

s.starttls()



# 계정 로그인을 위해서는 계정과 비밀번호가 필요하다. 하지만 테스트 코드에서 비밀번호를 표시하지만. github에서는 표시되면 안될 것이다.
# 계정, 비밀번호는 바꿀것이다.(예시 코드로 대체)
# 비밀번호는 계정 비밀 번호를 쓰면 안돼고, 앱 비밀번호를 만들어서 코드를 작성해야 한다..
s.login('seunghoon.no.1@gmail.com','fmerobepqjdttbot')

# :27 은 본문 작성 코드 입니다.
msg = MIMEText('내용: 본문 내용 텍스트 입니다. 테스트 중입니다.')
# 제목 코드입니다.
msg['Subject'] = '제목: 메일 보내기 테스트입니다.'

# seunghoon.no.1@gmail.com 에서 ilgu4193@gmail.com 로 메시지를 하나 보낸다.
s.sendmail('seunghoon.no.1@gmail.com','ilgu4193@gmail.com', msg.as_string())

s.quit()

