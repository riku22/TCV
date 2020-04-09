# -*- coding: utf-8 -*-
# ツイキャスライブ接続･切断等モジュール

from twitcasting.twitcasting import *
import views.main
import datetime

class connection:
	def __init__(self, userId):
		self.userId = userId
		userInfo = GetUserInfo(self.userId)
		self.movieId = userInfo["user"]["last_movie_id"]
		self.commentToSns = 0

	def getInitialComment(self, number):
		offset = max(0, number-50)
		limit = min(50, number)
		result = GetComments(self.movieId, offset, limit)
		self.lastCommentId = result[0]["id"]
		result2 = self.getComment()
		result3 = result2 + result
		result3.reverse()
		return result3

	def getComment(self):
		ret = []
		result = GetComments(self.movieId, 0, 50, self.lastCommentId)
		while result != []:
			self.lastCommentId = result[0]["id"]
			ret = result + ret
			result = GetComments(self.movieId, 0, 50, self.lastCommentId)
		ret.reverse()
		return ret

	def getLiveInfo(self):
		result = GetMovieInfo(self.movieId)
		return result

	def postComment(self, body):
		result = PostComment(self.movieID, body, self.commentToSns)
		return result

