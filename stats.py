from collections import defaultdict
import os
import climb_scoring
import data_import
import logbook

def summarise_stats(log: logbook.Logbook, scoring_method: climb_scoring.ScoringMethod):
    scores_by_type = defaultdict(list)
    failed_entries = 0
    for entry in log.ascents:
        try:
            entry_score = scoring_method.score_ascent(entry, log)
        except AttributeError:
            failed_entries += 1
        else:
            scores_by_type[entry.type].append(entry_score)
    
    header_str = f'{"Type":8}{"Count":>8}{"Total":>8}{"Mean":>8}'
    print("-"*len(header_str))
    print(header_str)
    print("-"*len(header_str))

    total_climbs = 0
    total_score = 0
    for climb_type in sorted(scores_by_type, key=lambda t:t if t is not None else ""): # Custom key allows sorting of NoneType entries
        if climb_type is None:
            climb_type = "None"
        scores = scores_by_type[climb_type]
        total_climbs += len(scores)
        total_score += sum(scores)
        if total_climbs > 0: # Only bother printing things with an actual score
            print(f"{climb_type:8}{len(scores):8}{sum(scores):8.1f}{sum(scores)/len(scores):8.2f}")
    mean_overall = total_score / total_climbs
    print("-"*len(header_str))
    print(f"{'ALL':8}{total_climbs:8}{total_score:8.1f}{mean_overall:8.2f}")
    print("-"*len(header_str))

def best_days(log: logbook.Logbook, scoring_method: climb_scoring.ScoringMethod, n=-1):
    """
    Returns the highest scoring n days in the logbook

    Args:
        log (logbook.Logbook): The logbook to check
        scoring_method (climb_scoring.ScoringMethod): The scoring method to use
        n (int): The number of entries to return. Defaults to returning all

    Returns:
        ?
    """
    daily_scores = defaultdict(list) # Should be {date: [scores]}

    for ascent in log.ascents:
        entry_score = scoring_method.score_ascent(ascent, log)
        date = ascent.date
        daily_scores[date].append(entry_score)
    
    summed_scores = {}
    for day, scores in daily_scores.items():
        full_day_score = sum(scores)
        summed_scores[day] = full_day_score

    dates_sorted_by_score = sorted(daily_scores.keys(), key=lambda x:sum(daily_scores[x]))

    combined_score_and_dates = [(date, summed_scores[date]) for date in dates_sorted_by_score]
    
    return combined_score_and_dates[-n:][::-1]


def main():
    file_relative_location = "data"
    file_name = "Carl_Logbook(1).xlsx"
    full_path = os.path.join(file_relative_location, file_name)

    log = data_import.UKCImport.import_from_xlsx(full_path, "Carl")

    summarise_stats(log, climb_scoring.FlatScoring)

    for day in best_days(log, climb_scoring.FlatScoring, 30):
        print(day)


if __name__ == "__main__":
    main()