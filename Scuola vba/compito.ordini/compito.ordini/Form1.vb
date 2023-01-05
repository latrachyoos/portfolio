Public Class Form1

    Private Sub Form1_Load(sender As System.Object, e As System.EventArgs) Handles MyBase.Load
        dgv.Rows.Clear()
        carica()
    End Sub

    Structure stcOrdine
        Dim IDOrdine As Integer
        <VBFixedString(50)> Dim NomeProdotto As String
        Dim PrezzoUnitaro As Decimal
        Dim Quantità As Integer
        Dim Sconto As Decimal
    End Structure

    Dim File As String = "vendite.csv"
    Dim Lrec As Integer
    Sub carica()
        Dim S() As String
        Dim O As stcOrdine
        Dim i As Integer = 1
        Lrec = Len(O)
        FileOpen(1, File, OpenMode.Input)
        FileOpen(2, "ordini.rnd", OpenMode.Random, , , Lrec)
        Do While Not EOF(1)
            S = Split(LineInput(1), ";")
            O.IDOrdine = S(0)
            O.NomeProdotto = S(1)
            O.PrezzoUnitaro = S(2)
            O.Quantità = S(3)
            O.Sconto = S(4)
            FilePut(2, O, i)
            caric(O)
            cari(O.IDOrdine)
            i += 1
        Loop
        FileClose(1)
        FileClose(2)
    End Sub

    Sub caric(ByVal O As stcOrdine)
        Dim n As Integer = dgv.Rows.Count
        dgv.Rows.Add()
        dgv.Rows(n).Cells("ID").Value = O.IDOrdine
        dgv.Rows(n).Cells("Nome").Value = O.NomeProdotto
        dgv.Rows(n).Cells("Quantità").Value = O.PrezzoUnitaro
        dgv.Rows(n).Cells("Prezzo").Value = O.Quantità
        dgv.Rows(n).Cells("Sconto").Value = O.Sconto
    End Sub

    Sub cari(ByVal id As Integer)
        Dim add As Boolean = True
        Dim N As Integer = ComboBox1.Items.Count
        Dim i As Integer
        If N > 0 Then
            Do
                If id =  ComboBox1.Items(i) Then
                    add = False
                End If
                i += 1
            Loop Until Not add Or i > N - 1
        End If
        If add Then
            ComboBox1.Items.Add(id)
        End If
    End Sub

    Private Sub Button1_Click(sender As System.Object, e As System.EventArgs) Handles Button1.Click
        car()
    End Sub

    Sub car()
        Dim R As stcOrdine
        Dim somma As Integer
        dgv.Rows.Clear()
        FileOpen(1, "ordini.rnd", OpenMode.Random, , , Lrec)
        For i = 1 To LOF(1) \ Lrec
            FileGet(1, R, i)
            If R.IDOrdine = ComboBox1.Text Then
                caric(R)
                somma += R.Quantità * R.PrezzoUnitaro - (R.Quantità * R.PrezzoUnitaro * R.Sconto / 100)
            End If
        Next
        FileClose(1)
        TextBox1.Text = somma
    End Sub

    Sub sommaTot()

    End Sub
End Class
'Significato dei campi presenti nel file CSV:
'IDOrdine;NomeProdotto;
'PrezzoUnitario;Quantita;Sconto


'a) Importare in un file random i dati presenti nel file csv

'b) visualizzare tutti i record in una datagridview



'C) Inserire un filtro che visualizza nella dgv i dati di un solo ordine mostrando in una casella di testo l'importo totale dell'ordine medesimo


'D). Caricare in un array di record tutti gli ordini con l'importo totale. Utilizzare i campi IDRecord, totaleOrdine (da calcolare per ciascun ordine).
'Volendo si può aggiungere il numero di prodotti dell'ordine (intesi come numero di prodotti differenti e non come somma di tutte le quantità)


'E) Visualizzare in una listbox tutti gli ordini il cui importo totale è inferiore ad un valore inserito dall'utente in una listbox
'F) Individuare l'ordine che presenta l'importo maggiore. Nota: l'importo maggiore potrebbe essere relativo a più ordini, pertanto il risultato deve essere visualizzato in una listbox.


'F. individuare  tutti i dati relativi alle vendite di un prodotto selezionato mediante casella a discesa (dove sono presenti tutti i prodotti senza ripetizioni) oppure un prodotto inserito dall'utente in una casella di testo

