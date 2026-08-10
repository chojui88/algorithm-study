def solution(genres, plays):
    genre_play = {}   # 장르별 총 재생수
    genre_song = {}   # 장르별 노래 (고유번호, 재생수)

    # 1. 장르별 총 재생수와 노래 목록 저장
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]

        # 장르별 총 재생수
        genre_play[genre] = genre_play.get(genre, 0) + play

        # 장르별 노래 저장
        if genre not in genre_song:
            genre_song[genre] = []

        genre_song[genre].append((i, play))

    # 2. 장르를 총 재생수 기준으로 내림차순 정렬
    sorted_genres = sorted(
        genre_play.keys(),
        key=lambda x: genre_play[x],
        reverse=True
    )

    answer = []

    # 3. 각 장르마다
    for genre in sorted_genres:

        # 재생수 내림차순
        # 재생수가 같으면 고유번호 오름차순
        songs = sorted(
            genre_song[genre],
            key=lambda x: (-x[1], x[0])
        )

        # 최대 2곡만 추가
        for song in songs[:2]:
            answer.append(song[0])

    return answer

    # 장르 내에서 많이 재생된 노래!!! g
    # 장르 내에서 재생 횟수 같으면, 고유 번호가 낮은 노래!!!