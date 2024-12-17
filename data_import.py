from datasets import load_dataset

dataset = load_dataset('neuralcatcher/hateful_memes', split='train')

print(dataset[1000])