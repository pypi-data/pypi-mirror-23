class Either:
    """
    The Either type represents values with two possibilities: B value of type Either<A, B> is either Left<A> or Right<B>
    But not both in the same time.
    """
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value and self.is_right() == other.is_right()


class Left(Either):

    def map(self, left_fn, right_fn):
        """
        takes 2 functions and applied first one on current Either value and returns new left Either mapped value
        :param left_fn: mapper for left value of Either
        :type (A) -> B
        :param right_fn: mapper for right value of Either, never called
        :type: (Any) -> Any
        :return: Left<B>
        """
        return Left(left_fn(self.value))

    def fold(self, left_fn, right_fn):
        """
        takes 2 functions and applied first one on current Either value and returns mapped value
        :param left_fn: mapper for left value of Either
        :type (A) -> B
        :param right_fn: mapper for right value of Either, never called
        :type: (Any) -> Any
        :return: B
        """
        return left_fn(self.value)

    def is_left(self):
        """
        :return: Boolean
        """
        return True


    def is_right(self):
        """
        :return: Boolean
        """
        return False


class Right(Either):

    def map(self, left_fn, right_fn):
        """
        takes 2 functions and applied second one on current Either value and returns new left Either mapped value
        :param left_fn: mapper for left value of Either, never called
        :type: (Any) -> Any
        :param right_fn: mapper for right value of Either
        :type (A) -> B
        :return: Left<B>
        """
        return Right(right_fn(self.value))

    def fold(self, left_fn, right_fn):
        """
        takes 2 functions and applied second one on current Either value and returns mapped value
        :param left_fn: mapper for left value of Either, never called
        :type: (Any) -> Any
        :param right_fn: mapper for right value of Either
        :type (A) -> B
        :return: Left<B>
        """
        return right_fn(self.value)

    def is_right(self):
        """
        :return: Boolean
        """
        return True

    def is_left(self):
        """
        :return: Boolean
        """
        return False