# Масив з URL вебсайтів для перевірки
websites=("https://google.com" "https://facebook.com" "https://twitter.com" "https://x.com")

# Ім'я файлу для логів
log_file="website_status.log"

# Очищення попередніх логів
> $log_file

# Перевірка доступності кожного вебсайту
for site in "${websites[@]}"
do
    # Використовуємо curl для перевірки статусу з перенаправленням
    status_code=$(curl -o /dev/null -s -w "%{http_code}\n" --location $site)

    # Перевіряємо, чи статус код 200
    if [ $status_code -eq 200 ]; then
        echo "$site is UP" >> $log_file
    else
        echo "$site is DOWN" >> $log_file
    fi
done

# Виведення повідомлення про успішне записування логів
echo "Результати перевірки записані у файл: $log_file"
