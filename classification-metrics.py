import os
import random

def generate_dataset(size=100):
    """Generate a synthetic binary classification dataset."""
    actual = [random.choice([0, 1]) for _ in range(size)]
    predicted = [random.choice([0, 1]) for _ in range(size)]
    return actual, predicted

def create_confusion_matrix(actual, predicted):
    """Create a confusion matrix from the dataset."""
    TP = sum(1 for a, p in zip(actual, predicted) if a == 1 and p == 1)
    TN = sum(1 for a, p in zip(actual, predicted) if a == 0 and p == 0)
    FP = sum(1 for a, p in zip(actual, predicted) if a == 0 and p == 1)
    FN = sum(1 for a, p in zip(actual, predicted) if a == 1 and p == 0)
    return TP, TN, FP, FN

def calculate_accuracy(TP, TN, FP, FN):
    return (TP + TN) / (TP + TN + FP + FN) * 100

def calculate_precision(TP, FP):
    return (TP / (TP + FP) * 100) if (TP + FP) != 0 else 0

def calculate_recall(TP, FN):
    return (TP / (TP + FN) * 100) if (TP + FN) != 0 else 0

def calculate_specificity(TN, FP):
    return (TN / (TN + FP) * 100) if (TN + FP) != 0 else 0

def calculate_error_rate(FP, FN, TP, TN):
    return ((FP + FN) / (TP + TN + FP + FN)) * 100

def calculate_f1_score(precision, recall):
    return (2 * (precision * recall) / (precision + recall)) if (precision + recall) != 0 else 0

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    actual, predicted = generate_dataset(100)
    TP, TN, FP, FN = create_confusion_matrix(actual, predicted)
    
    while True:
        clear_screen()
        print("Menu:")
        print("1. Show Confusion Matrix Values")
        print("2. Accuracy")
        print("3. Precision")
        print("4. Recall")
        print("5. Specificity")
        print("6. Error Rate")
        print("7. F1 Score")
        print("8. Regenerate Dataset")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            print("Confusion Matrix:")
            print(f"TP: {TP}, TN: {TN}, FP: {FP}, FN: {FN}")
        elif choice == '2':
            print(f"Accuracy: {calculate_accuracy(TP, TN, FP, FN):.2f}%")
        elif choice == '3':
            print(f"Precision: {calculate_precision(TP, FP):.2f}%")
        elif choice == '4':
            print(f"Recall: {calculate_recall(TP, FN):.2f}%")
        elif choice == '5':
            print(f"Specificity: {calculate_specificity(TN, FP):.2f}%")
        elif choice == '6':
            print(f"Error Rate: {calculate_error_rate(FP, FN, TP, TN):.2f}%")
        elif choice == '7':
            precision = calculate_precision(TP, FP)
            recall = calculate_recall(TP, FN)
            print(f"F1 Score: {calculate_f1_score(precision, recall):.2f}%")
        elif choice == '8':
            actual, predicted = generate_dataset(100)
            TP, TN, FP, FN = create_confusion_matrix(actual, predicted)
            print("New dataset generated.")
            print("Confusion Matrix:")
            print(f"TP: {TP}, TN: {TN}, FP: {FP}, FN: {FN}")
        elif choice == '0':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        
        input("\nPress any key to continue...")

if __name__ == "__main__":
    main()
