Public Class Form1
    Dim R As Integer = 6
    Dim C As Integer = 7
    Dim M(R - 1, C - 1) As Integer
    Dim giocatore As Integer = 1
    Dim T As Integer = 0
    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        dgvF4.Columns.Clear()
        dgvF4.Rows.Clear()
        dgvF4.ColumnCount = C
        dgvF4.Rows.Add(R - 1)
        For i = 0 To R - 1
            For k = 0 To C - 1
                M(i, k) = 0
            Next
        Next
    End Sub

    Sub vittoria()
        MessageBox.Show("sei un gay ma hai vinto")
        dgvF4.Enabled = False
    End Sub

    Sub visua(ByVal mossa As Integer, ByVal IND As Integer)
        dgvF4.Rows(R - IND).Cells(mossa).Value = M(R - IND, mossa)
        T += 1
        If T > 6 Then
            controlla(mossa, IND)
        End If
    End Sub

    Sub controlla(ByVal mossa As Integer, ByVal IND As Integer)
        If riga(IND) Or colonna(mossa) Then
            vittoria()
        End If
        If T > 10 Then
            If diagonale(mossa, IND) Then
                vittoria()
            End If
        End If
    End Sub

    Function riga(ByVal IND As Integer) As Boolean
        Dim CNT As Boolean
        Dim i, col As Integer
        Do
            If M(R - IND, col) = giocatore Then
                i += 1
            Else
                i = 0
            End If
            If i = 4 Then
                CNT = True
            End If
            col += 1
        Loop Until CNT Or col > C - 1
        Return CNT
    End Function

    Function colonna(ByVal mossa As Integer) As Boolean
        Dim CNT As Boolean
        Dim i, rig As Integer
        Do
            If M(rig, mossa) = giocatore Then
                i += 1
            Else
                i = 0
            End If
            If i = 4 Then
                CNT = True
            End If
            rig += 1
        Loop Until CNT Or rig > R - 1
        Return CNT
    End Function

    Function diagonale(ByVal mossa As Integer, ByVal IND As Integer) As Boolean
        Dim somma, i, cont As Integer
        Dim CNT As Boolean = True
        If IND > mossa Then
            somma = R - IND + mossa
            If somma >= 4 Then
                Do While CNT And i < R And cont < 4
                    If M(IND - mossa + i, i) = giocatore Then
                        i += 1
                        cont += 1
                    Else
                        CNT = False
                    End If
                Loop
            End If
            'ElseIf IND < mossa Then
            '    somma = C - mossa + IND
            '    If somma >= 4 Then
            '        Do While CNT And i < C And cont < 4

            '        Loop
            '    End If
            'Else

        End If
        Return CNT
    End Function

    Sub tocco()
        Dim mossa As Integer
        mossa = dgvF4.CurrentCell.ColumnIndex
        gioco(mossa)
    End Sub

    Sub gioco(ByVal mossa As Integer)
        Dim CNT As Boolean
        Dim IND As Integer = 1
        Do While Not CNT And IND < R + 1
            If M(R - IND, mossa) = 0 Then
                CNT = True
                M(R - IND, mossa) = giocatore
                visua(mossa, IND)
            Else
                IND += 1
            End If
        Loop
        cambia()
    End Sub

    Sub cambia()
        If giocatore = 1 Then
            giocatore = 2
        Else
            giocatore = 1
        End If
    End Sub

    Private Sub DataGridView1_CellContentClick(ByVal sender As System.Object, ByVal e As System.Windows.Forms.DataGridViewCellEventArgs) Handles dgvF4.CellClick
        tocco()
    End Sub
End Class
'data matrice 6 righe e sette colonne visualizzata in una dgv riempire 
'la matrice alternando i valori due e uno partendo dal fondo della colonna 
'su cui l'utente ha fatto click 