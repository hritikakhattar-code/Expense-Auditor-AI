from app.nlp_analysis import analyze_description

def rule_based_flags(df):
    flags = []
    seen_receipts = set()

    for _, row in df.iterrows():
        issues = []

        # Rule-based flags (Example rules based on the new CSV categories)
        if row['Amount'] > 1000:  # Large expenses
            issues.append("High amount")
        
        if row['Category'] == "Consulting" and row['Amount'] > 500:  # Consulting fee check
            issues.append("Consulting fee is high")
        
        if row['Category'] == "Meals" and row['Amount'] > 100:  # Meals limit check
            issues.append("Meals cost exceeded")
        
        if row['Receipt Number'] in seen_receipts:  # Duplicate receipt check
            issues.append("Duplicate receipt")
        seen_receipts.add(row['Receipt Number'])

        # NLP Analysis on the Description field (optional)
        description = row['Description']
        nlp_label, nlp_score = analyze_description(description)

        if nlp_label in ["consulting", "client", "training", "office supplies", "travel", "entertainment"]:
            issues.append(f"Suspicious category: {nlp_label} ({nlp_score:.2f})")

        flags.append(", ".join(issues) if issues else "OK")

    df['Flags'] = flags
    return df
