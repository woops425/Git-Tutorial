# 사용자로부터 원의 반지름을 '정수'로 입력 받아 그 원의 넓이를 구하는 프로그램 작성
# 실행  예시 : 넓이를 구하고자 하는 원의 반지름은? 4
# 반지름 4인 원의 넓이 = 3.14 * 4 * 4 = 50.24

# 조건 1 : 함수 get_radius()를 정의 후 '호출'해야함
# get_radius()는 매개변수 prompt로 전달받은 메시지를 화면에 출력 후 입력된 값을 정수로 변환해 호출측으로 반환하는 함수
# def get_radius(prompt):
#         r = int(input(prompt))
#         return r

# 조건 2 : 함수 get_circle_area()를 정의 후 '호출'
# get_circle_area()는 넓이를 구하고자 하는 원의 반지름을 전달받아, 구한 원의 넓이를 호출 측으로 반환하는 함수

def get_radius(prompt) :
    r = int(input(prompt))
    return r 

def get_circle_area(radius) :
    area = 3.14 * radius * radius
    return area

radius = get_radius("넓이를 구하고자 하는 원의 반지름은? ")
circle_area = get_circle_area(radius)

print("반지름 {0}인 원의 넓이 = 3.14 * {0} * {0} = {1}".format(radius,circle_area))