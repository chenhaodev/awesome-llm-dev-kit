#this script test the bug/no-bug-issue when pretraining llm on datasets using llama-factory
#1. pile, bug
#2. wiki demo, no bug

CUDA_VISIBLE_DEVICES=0 python src/train_bash.py \
    --stage pt \
    --do_train True \
    --model_name_or_path Qwen/Qwen1.5-0.5B \
    --finetuning_type full \
    --template default \
    --dataset_dir data \
    --dataset c4_demo \
    --cutoff_len 1024 \
    --learning_rate 5e-05 \
    --num_train_epochs 1.0 \
    --max_samples 500000 \
    --per_device_train_batch_size 2 \
    --gradient_accumulation_steps 8 \
    --lr_scheduler_type cosine \
    --max_grad_norm 1.0 \
    --logging_steps 5 \
    --save_steps 100 \
    --warmup_steps 20 \
    --neftune_noise_alpha 0.5 \
    --optim adamw_torch \
    --packing True \
    --output_dir saves/Qwen1.5-0.5B/full/train_2024-03-23-09-49-40 \
    --fp16 True \
    --plot_loss True

