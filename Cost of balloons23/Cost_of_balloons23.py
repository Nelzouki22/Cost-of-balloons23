def min_balloon_cost():
    t = int(input())  # عدد حالات الاختبار

    for _ in range(t):
        green_cost, purple_cost = map(int, input().split())  # تكلفة البالونات الخضراء والبنفسجية
        n = int(input())  # عدد المشاركين

        participants = []
        for _ in range(n):
            participants.append(list(map(int, input().split())))  # إدخال حالة كل مشارك

        # حساب التكلفة لكل سيناريو
        first_scenario_cost = 0
        second_scenario_cost = 0

        for p in participants:
            first_scenario_cost += p[0] * green_cost + p[1] * purple_cost
            second_scenario_cost += p[0] * purple_cost + p[1] * green_cost

        # طباعة أقل تكلفة بين السيناريوهين
        print(min(first_scenario_cost, second_scenario_cost))

# استدعاء الدالة
min_balloon_cost()

