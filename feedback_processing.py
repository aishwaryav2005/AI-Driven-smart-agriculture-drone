def process_feedback(analysis):
    health_status = analysis.get('health', 'Unknown')
    issues = analysis.get('issues_detected', False)
    suggestions = analysis.get('suggestions', 'No suggestions available.')

    print(f"Plant Health Status: {health_status}")
    if issues:
        print("Issues detected!")
    print(f"Suggestions: {suggestions}")
