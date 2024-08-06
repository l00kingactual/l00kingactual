import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import ttest_rel, wilcoxon, ks_2samp
import os

# Load results
baseline_costs = np.load('baseline_costs.npy')
enhanced_costs = np.load('enhanced_costs.npy')

def calculate_metrics(costs):
    return {
        'Mean': np.mean(costs),
        'Median': np.median(costs),
        'Standard Deviation': np.std(costs),
        'Min': np.min(costs),
        'Max': np.max(costs)
    }

def plot_comparison(baseline_costs, enhanced_costs):
    # Ensure directories exist
    os.makedirs('images/aco_plots', exist_ok=True)

    plt.figure(figsize=(15, 15))

    # 2D Line Plot with Trend Lines
    plt.subplot(3, 2, 1)
    plt.plot(baseline_costs, label='Baseline ACO', color='blue')
    plt.plot(enhanced_costs, label='Enhanced ACO', color='green')
    plt.xlabel('Run Index')
    plt.ylabel('Cost')
    plt.title('2D Line Plot of ACO Costs with Trend Lines')
    plt.legend()
    plt.grid(True)

    # Add trend lines
    z_baseline = np.polyfit(range(len(baseline_costs)), baseline_costs, 1)
    p_baseline = np.poly1d(z_baseline)
    plt.plot(range(len(baseline_costs)), p_baseline(range(len(baseline_costs))), "r--", label='Baseline Trend Line')

    z_enhanced = np.polyfit(range(len(enhanced_costs)), enhanced_costs, 1)
    p_enhanced = np.poly1d(z_enhanced)
    plt.plot(range(len(enhanced_costs)), p_enhanced(range(len(enhanced_costs))), "y--", label='Enhanced Trend Line')

    plt.legend()

    # Box Plot
    plt.subplot(3, 2, 2)
    plt.boxplot([baseline_costs, enhanced_costs], labels=['Baseline ACO', 'Enhanced ACO'])
    plt.ylabel('Cost')
    plt.title('Box Plot of ACO Costs')

    # Metrics table
    baseline_metrics = calculate_metrics(baseline_costs)
    enhanced_metrics = calculate_metrics(enhanced_costs)
    metrics_df = pd.DataFrame([baseline_metrics, enhanced_metrics], index=['Baseline ACO', 'Enhanced ACO'])

    plt.subplot(3, 2, 3)
    plt.axis('tight')
    plt.axis('off')
    plt.table(cellText=metrics_df.values,
              colLabels=metrics_df.columns,
              rowLabels=metrics_df.index,
              cellLoc='center', loc='center')
    plt.title('Metrics Table')

    # Metrics Bar Chart
    plt.subplot(3, 2, 4)
    metrics_df.T.plot(kind='bar', ax=plt.gca())
    plt.title('Metrics Bar Chart')
    plt.xticks(rotation=45)

    # Convergence Plot with Trend Lines
    plt.subplot(3, 2, 5)
    plt.plot(np.minimum.accumulate(baseline_costs), label='Baseline ACO', color='blue')
    plt.plot(np.minimum.accumulate(enhanced_costs), label='Enhanced ACO', color='green')
    plt.xlabel('Run Index')
    plt.ylabel('Best Cost')
    plt.title('Convergence Plot with Trend Lines')
    plt.legend()
    plt.grid(True)

    # Add trend lines to convergence plot
    z_baseline_conv = np.polyfit(range(len(baseline_costs)), np.minimum.accumulate(baseline_costs), 1)
    p_baseline_conv = np.poly1d(z_baseline_conv)
    plt.plot(range(len(baseline_costs)), p_baseline_conv(range(len(baseline_costs))), "r--", label='Baseline Convergence Trend Line')

    z_enhanced_conv = np.polyfit(range(len(enhanced_costs)), np.minimum.accumulate(enhanced_costs), 1)
    p_enhanced_conv = np.poly1d(z_enhanced_conv)
    plt.plot(range(len(enhanced_costs)), p_enhanced_conv(range(len(enhanced_costs))), "y--", label='Enhanced Convergence Trend Line')

    plt.legend()

    plt.tight_layout()
    plt.savefig('images/aco_plots/aco_comparison_plots_with_metrics.png')
    plt.show()

    # 3D Surface Plot
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    X, Y = np.meshgrid(np.linspace(0, len(baseline_costs)-1, len(baseline_costs)), [0, 1])
    Z = np.array([baseline_costs, enhanced_costs])

    surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
    ax.set_xlabel('Run Index')
    ax.set_ylabel('ACO Type')
    ax.set_zlabel('Cost')
    ax.set_yticks([0, 1])
    ax.set_yticklabels(['Baseline', 'Enhanced'])
    ax.set_title('3D Surface Plot of ACO Costs')
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.savefig('images/aco_plots/aco_3d_surface_plot_smooth.png')
    plt.show()

    # Statistical Testing
    t_stat, p_value_ttest = ttest_rel(baseline_costs, enhanced_costs)
    wilcoxon_stat, p_value_wilcoxon = wilcoxon(baseline_costs, enhanced_costs)
    ks_stat, p_value_ks = ks_2samp(baseline_costs, enhanced_costs)
    
    print(f"Paired t-test: t-statistic = {t_stat}, p-value = {p_value_ttest}")
    print(f"Wilcoxon signed-rank test: statistic = {wilcoxon_stat}, p-value = {p_value_wilcoxon}")
    print(f"Kolmogorov-Smirnov test: statistic = {ks_stat}, p-value = {p_value_ks}")
    
    if p_value_ttest < 0.05:
        print("The differences are statistically significant according to the t-test (p < 0.05).")
    else:
        print("The differences are not statistically significant according to the t-test (p >= 0.05).")
    
    if p_value_wilcoxon < 0.05:
        print("The differences are statistically significant according to the Wilcoxon test (p < 0.05).")
    else:
        print("The differences are not statistically significant according to the Wilcoxon test (p >= 0.05).")
    
    if p_value_ks < 0.05:
        print("The differences are statistically significant according to the Kolmogorov-Smirnov test (p < 0.05).")
    else:
        print("The differences are not statistically significant according to the Kolmogorov-Smirnov test (p >= 0.05).")

    # Save metrics
    metrics_df.to_csv('aco_metrics_detailed.csv')

if __name__ == '__main__':
    plot_comparison(baseline_costs, enhanced_costs)
