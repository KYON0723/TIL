from faker import Faker

fake = Faker('ko_KR')


fake.seed_instance(4321)

print('1번')
print(fake.name())
print(fake.name())
print(fake.name())
print(fake.name())

print('2번')
fake2 = Faker('ko_KR')
print(fake2.name())
print(fake2.name())
print(fake2.name())
print(fake2.name())