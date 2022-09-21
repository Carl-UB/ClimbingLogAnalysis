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
    for climb_type in sorted(scores_by_type):
        scores = scores_by_type[climb_type]
        total_climbs += len(scores)
        total_score += sum(scores)
        print(f"{climb_type:8}{len(scores):8}{sum(scores):8.1f}{sum(scores)/len(scores):8.2f}")
    mean_overall = total_score / total_climbs
    print("-"*len(header_str))
    print(f"{'ALL':8}{total_climbs:8}{total_score:8.1f}{mean_overall:8.2f}")
    print("-"*len(header_str))

def best_n_days(log: logbook.Logbook, scoring_method: climb_scoring.ScoringMethod):
    daily_scores = defaultdict(list)


def main():
    file_relative_location = "data"
    file_name = "Carl_Logbook(1).xlsx"
    full_path = os.path.join(file_relative_location, file_name)

    log = data_import.UKCImport.import_from_xlsx(full_path, "Carl")

    summarise_stats(log, climb_scoring.FlatScoring)


if __name__ == "__main__":
    main()