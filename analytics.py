import pandas as pd
import numpy as np

def task_analytics(tasks):

    df = pd.DataFrame(tasks)

    total = len(df)

    completed = len(df[df['status'] == 'Completed'])

    pending = len(df[df['status'] == 'Pending'])

    percentage = np.round((completed / total) * 100, 2) if total > 0 else 0

    return {
        'total_tasks': total,
        'completed_tasks': completed,
        'pending_tasks': pending,
        'completion_percentage': percentage
    }
