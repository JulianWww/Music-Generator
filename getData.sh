if [ ! -f .env ]
then
  export $(cat .env | xargs)
fi

#spotify_dl -l https://open.spotify.com/playlist/4GtQVhGjAwcHFz82UKy3Ca?si=6fe1f1b6ad4f4b93 -o .data

idx=0
rm -r data
mkdir data
for i in .data/*/*.mp3; do 
    ffmpeg -i "$i" -c:a pcm_f32le "data/${idx}.wav"
    python3 -c "from utility import preprocess_data; preprocess_data($idx)"
    ((idx++))
done

echo "{\"count\":$idx}" > data/config.json