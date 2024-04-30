import matplotlib.pyplot as plt


def evaluate(Y, Y_H, arrangement_prompts=False):
    predictions = [evaluate_prompt(y, y_hat) for y, y_hat in zip(Y, Y_H)]
    accuracy = sum(predictions) / len(predictions)
    return accuracy


def evaluate_prompt(y, y_hat, arrangement_prompt=False):
    if arrangement_prompt:
        for arrangement in y_hat:
            if arrangement not in y:
                return False
        return True

    # Either num of arrangements n==m OR answer == gold answer
    return y_hat.lower() == y.lower()


def plot_results(results, title='Performance on Different Setups'):
    setups = [item[0] for item in results]
    accuracies = [item[1] for item in results]

    plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
    bars = plt.bar(setups, accuracies, color='skyblue', alpha=0.7, width=0.4)  # Adjust width for thinner bars
    plt.xlabel('Setups')
    plt.ylabel('Accuracy')
    plt.title(title)

    # Rotating x-axis labels diagonally
    plt.xticks(rotation=45, ha='right')

    # Adding text labels near the bars
    for i, bar in enumerate(bars):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f"{accuracies[i]:.2f}", ha='center', va='bottom',
                 fontweight='bold')

    # Display the plot
    plt.tight_layout()
    plt.grid()
    plt.savefig('fig.png')
    plt.show()


if __name__ == '__main__':
    results = [("with frenhfries", 0.56), ("with disambiguate", 0.22), ("without disamibugate", 0.89),
               ("without cola", 0.68)]
    plot_results(results)
