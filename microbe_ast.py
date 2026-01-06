"""
MicrobeAST: Bacterial Sensitivity Analyzer

A Python-based utility that interprets AST inhibition zones based on 
CLSI M100-Ed36 (2026) standards for laboratory automation.
Author: [Asma Rafiq]
"""

# Global Breakpoints (These numbers are based on clinical consensus)
SUSCEPTIBLE_MM = 21
RESISTANT_MM = 15

def get_clinical_status(zone_mm):
    """Interprets the inhibition zone diameter to determine clinical status (S/I/R)."""
    if zone_mm >= SUSCEPTIBLE_MM:
        return "S (Susceptible)"
    elif zone_mm > RESISTANT_MM:
        return "I (Intermediate)"
    else:
        return "R (Resistant)"

def generate_report(lab_database):
    """Processes lab data and prints a formatted clinical report with a summary."""
    resistant_count = 0
    total_tests = 0
    
    print(f"\n{'CLINICAL MICROBIOLOGY AST REPORT (2026)':^60}")
    print("=" * 60)
    print(f"{'SAMPLE ID':<15} | {'ANTIBIOTIC':<15} | {'ZONE':<6} | {'STATUS'}")
    print("-" * 60)

    for sample, tests in lab_database.items():
        for antibiotic, zone in tests.items():
            status = get_clinical_status(zone)
            total_tests += 1
            if "Resistant" in status:
                resistant_count += 1
            print(f"{sample:<15} | {antibiotic:<15} | {zone:<6} | {status}")
    
    print("=" * 60)
    print(f"SUMMARY: {total_tests} Tests Conducted | {resistant_count} Resistant Cases Found")
    print("Standard: CLSI M100 Guidelines | Date: 2026-01-06\n")

# --- MOCK LABORATORY DATA (Example Data Set) ---
if __name__ == "__main__":
    lab_results = {
        "BLOOD-7721": {"Ciprofloxacin": 25, "Amoxicillin": 12},
        "URINE-9904": {"Meropenem": 22, "Gentamicin": 18},
        "SPUTUM-115": {"Ceftriaxone": 14, "Azithromycin": 21}
    }
    generate_report(lab_results)
