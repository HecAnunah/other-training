# В американском футболе выигрыш может произойти несколькими способами.
# Эти оценки имеют разные значения, что приводит к оценкам, которые поднимаются на основе того, как команда забила.
# Команда может забить одним из следующих способов:
#     Забив приземление, которое набирает 6 очков. Приземление дает команде возможность добавить к своему счету, либо по:
#         Собираясь на 2 очка, что (как вы можете догадаться), заработает 2 балла, или Попытка ударить по дополнительной точке,
#         что заработает 1 очко.
#         Ни один из этих пунктов не гарантирован!
#     Выбивая полевой гол, который стоит 3 очка. Игрок, который занимается в их собственной конечной зоне,
#     называется безопасностью, и он стоит 2 очка. Подробнее о безопасности Мы только что вошли в игру посередине,
#     и мы хотели бы знать, как появился текущий счет.
#     Учитывая текущий счет, верните массив, содержащий все возможные способы, которыми команда могла бы получить текущий счет.
#     Массив должен содержать один или несколько объектов, которые выглядят так:
# {
#   td: 2,  // touchdowns = 6pts * 2
#   tp: 1,  // 2 point conversions = 2pts * 1
#   ep: 1,  // extra points = 1pts * 1
#   fg: 1,  // field goals = 3pts * 1
#   s:  0   // safeties = 2pts * 0
# } // 18 total points

def possible_scores(target_score):
    results = []

    # Ограничиваем максимальное количество каждого действия
    max_td = target_score // 6  # максимум тачдаунов
    max_fg = target_score // 3  # максимум филд-голов
    max_s = target_score // 2   # максимум сейфти

    # Перебор всех возможных комбинаций
    for td in range(max_td + 1):
        for tp in range(td + 1):  # TP может быть максимум столько, сколько TD
            for ep in range(td + 1):  # EP тоже ограничен количеством TD
                for fg in range(max_fg + 1):
                    for s in range(max_s + 1):
                        total_points = (6 * td) + (2 * tp) + (1 * ep) + (3 * fg) + (2 * s)

                        # Проверяем совпадение с целевым количеством очков
                        if total_points == target_score and (tp + ep) <= td:
                            results.append({
                                'td': td,  # touchdowns
                                'tp': tp,  # 2-point conversions
                                'ep': ep,  # extra points
                                'fg': fg,  # field goals
                                's': s     # safeties
                            })
    return results

# Пример использования
score = 6
combinations = possible_scores(score)
for combo in combinations:
    print(combo)


# Иные варианты

def score_breakdowns(score):
    arr = []
    max_td = score // 6
    for td in range(max_td+1):
        rem_score_td = score - 6*td
        max_fg = rem_score_td // 3
        for fg in range(max_fg+1):
            rem_score_fg = rem_score_td - 3*fg
            max_s = rem_score_fg // 2
            for s in range(max_s+1):
                rem_score_s = rem_score_fg - 2*s
                max_tp = min( rem_score_s // 2, td )
                for tp in range(max_tp+1):
                    rem_score_tp = rem_score_s - 2*tp
                    max_ep = min(rem_score_tp, td-tp)
                    if rem_score_tp - max_ep == 0:
                        arr.append( {"td":td, "tp":tp, "ep":max_ep, "fg":fg, "s":s} )
    return arr


def score_breakdowns(target_score):
    results = []
    max_td = target_score // 6
    max_fg = target_score // 3

    for td in range(max_td + 1):
        for tp in range(td + 1):  # 2-point conversions can't exceed touchdowns
            for ep in range(td + 1 - tp):  # extra points + 2-point conversions <= touchdowns
                for fg in range(max_fg + 1):
                    remaining = target_score - (6 * td + 2 * tp + ep + 3 * fg)
                    if remaining >= 0 and remaining % 2 == 0:
                        s = remaining // 2
                        results.append({"td": td, "tp": tp, "ep": ep, "fg": fg, "s": s})
    return results
